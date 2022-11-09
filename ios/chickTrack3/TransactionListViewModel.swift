//
//  TransactionListViewModel.swift
//  chickTrack3
//
//  Created by 김규진 on 2022/11/08.
//

import Foundation
import Combine
import UserNotifications

typealias TransactionPrefixSum = [Double]
var cumulativeSum = TransactionPrefixSum()
let notificationCenter = UNUserNotificationCenter.current()

final class TransactionListViewModel: ObservableObject {
    //값이 변경될때마다 사용자에게 알림
    @Published var transactions: [chickTrackJson] = []
    private var cancellables = Set<AnyCancellable>()
    
    init() {
        Timer.scheduledTimer(withTimeInterval: 10,repeats: true){
            (_) in
                self.getTransactions()
        }
    }
    
    
    func getTransactions() {
        guard let url = URL(string: "your Domain!!") else{
            print("invalid URL")
            return
        }
        
        
        URLSession.shared.dataTaskPublisher(for: url)
            .tryMap { (data, response) -> Data in
                guard let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode == 200 else {
                    dump(response)
                    throw URLError(.badServerResponse)
                }
                
                return data
            }
            .receive(on: DispatchQueue.main)
            .decode(type: [chickTrackJson].self, decoder: JSONDecoder())
            .sink { completion in
                switch completion {
                case .failure(let error):
                    print("Error fetching transactions:", error.localizedDescription)
                case .finished:
                    print("Finished fetching transactions")
                }
            } receiveValue: { [weak self]result in
                self?.transactions = result
                
            }
            .store(in: &cancellables)
    }
    
    func accumulateTransactions() -> TransactionPrefixSum {
        print("accumulateTransactions")
        guard !transactions.isEmpty else { return [] }
        let aoa = transactions.map{$0.amountofActivity}
        print("aoa:",aoa)
        let aoaresult = trunc(aoa[0])
//        print("totalAOA:",totalAoA)
        
        cumulativeSum.append(aoaresult)
        print("cumulativeSum:",cumulativeSum)
        
        
        let push = UNMutableNotificationContent()
        push.title = "ChickTracker"
        push.subtitle = "활동량 알림"
        push.body = "활동량이 목표치보다 높습니다"
        push.badge = 1
        print("cumulativelast: ",cumulativeSum.last)
        if cumulativeSum.last ?? 0 > 50 {
//            print("sendNotification")
//            let trigger = UNTimeIntervalNotificationTrigger(timeInterval: 3, repeats: false)
//            let request = UNNotificationRequest(identifier: "test", content: push, trigger: trigger)
//            UNUserNotificationCenter.current().add(request){ error in
//                if let error = error {
//                    print("Notification Error: ", error)
//                }
//            }
            sendNoti()
        }
        
        return cumulativeSum
    }
    
    func requestNotificationAuthorization() {
        let authOptions: UNAuthorizationOptions = [.alert, .sound, .badge]

        notificationCenter.requestAuthorization(options: authOptions) { success, error in
            if let error = error {
                print(error)
            }
        }
    }
    
    func sendNoti() {
        
        notificationCenter.removeAllPendingNotificationRequests()
        
        let push = UNMutableNotificationContent()
        push.title = "ChickTracker"
        push.subtitle = "활동량 알림"
        push.body = "활동량이 목표치보다 높습니다"
        push.badge = 1
        let trigger = UNTimeIntervalNotificationTrigger(timeInterval: 3, repeats: false)
        print("trigger:",trigger)
        let request = UNNotificationRequest(identifier: UUID().uuidString, content: push, trigger: trigger)
        print("request",request)
        print("sendNoti")
        notificationCenter.add(request) { (error) in
            if error != nil {
                print(error)
            }
        }
    }
}
