//
//  Extensions.swift
//  chickTrack3
//
//  Created by 김규진 on 2022/11/08.
//
import UserNotifications
import Foundation
import SwiftUI

extension Color {
    static let background = Color("Background")
    static let icon = Color("Icon")
    static let text = Color("Text")
    static let systemBackground = Color(uiColor: .systemBackground)
    
}

extension DateFormatter {
    static let allNumericKor: DateFormatter = {
        print("Initializing DateFormatter")
        let formatter = DateFormatter()
        formatter.dateFormat = "yyyyMMDD"
        
        return formatter
    }()
}

extension String {
    func dateParsed() -> Date {
        guard let parseDate = DateFormatter.allNumericKor.date(from: self) else { return Date() }
        
        return parseDate
    }
}

extension Date : Strideable {
    func formatted() -> String {
        return self.formatted(.dateTime.year().month().day())
    }
}


struct ViewDidLoadModifier: ViewModifier {

    @State private var didLoad = false
    private let action: (() -> Void)?

    init(perform action: (() -> Void)? = nil) {
        self.action = action
    }

    func body(content: Content) -> some View {
        content.onAppear {
            if didLoad == false {
                didLoad = true
                action?()
            }
        }
    }

}

extension View {

    func onLoad(perform action: (() -> Void)? = nil) -> some View {
        modifier(ViewDidLoadModifier(perform: action))
    }

}


extension AppDelegate : UNUserNotificationCenterDelegate {
    // 앱이 실행 중 일때 처리하는 메서드
    func userNotificationCenter(_ center: UNUserNotificationCenter, willPresent notification: UNNotification, withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
        completionHandler([.list, .banner])
    }
}


class AppDelegate : UIResponder, UIApplicationDelegate {
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
            UNUserNotificationCenter.current().delegate = self
            return true
        }
}
