//
//  chickTrack3App.swift
//  chickTrack3
//
//  Created by 김규진 on 2022/11/08.
//

import SwiftUI

@main
struct chickTrack3App: App {
    @StateObject var transactionListVM = TransactionListViewModel()
    

    
    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(transactionListVM)
                .onLoad(){
                    transactionListVM.requestNotificationAuthorization()
                }
                
        }
        
    }
    
    
    
    
}
