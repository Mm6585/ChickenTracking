//
//  ContentView.swift
//  ChickTracker
//
//  Created by 김규진 on 2022/11/04.
//

import SwiftUI
import SwiftUICharts



struct ContentView: View {
    @EnvironmentObject var transactionListVM : TransactionListViewModel
    var body: some View {
        NavigationView{
            ScrollView{
                
                // MARK: title
                VStack(alignment: .leading, spacing: 24){
                    Text("Dashboard")
                        .font(.title2)
                        .bold()
                    
                    
                    // MARK: chart
                    let data = transactionListVM.accumulateTransactions()
                    if !data.isEmpty{
                        let totalExpense = data.last ?? 0
                        
                        CardView{
                            VStack(alignment : .leading)  {
                                ChartLabel(totalExpense.formatted(), type: .title, format: "%.02f")
                                LineChart()
                            }
                            .background(Color.systemBackground)
                        }
                        .data(data)
                        .chartStyle(ChartStyle(backgroundColor: Color.systemBackground, foregroundColor: ColorGradient(Color.icon.opacity(0.4),Color.icon)))
                        .frame(height:300)
                    }
                    
                    
                    
                    RecentTransactionList()
                }
                .padding()
                .frame(maxWidth: .infinity)
                
            }
            .background(Color.background)
            .navigationBarTitleDisplayMode(.inline)
            .toolbar{
                ToolbarItem{
                    Image(systemName: "bell.badge")
                        .symbolRenderingMode(.palette)
                        .foregroundStyle(Color.icon,.primary)
                }
            }
        }
        .navigationViewStyle(.stack)
        .accentColor(.primary)
    }
}

struct ContentView_Previews: PreviewProvider {
    static let transactionListVM: TransactionListViewModel = {
        let transactionListVM = TransactionListViewModel()
        transactionListVM.transactions = transactionListPreviewData
        return transactionListVM
    }()
    
    static var previews: some View {
        Group {
            ContentView()
            ContentView()
                .preferredColorScheme(.dark)
        }
        .environmentObject(transactionListVM)
    }
}
