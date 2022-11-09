//
//  RecentTransactionList.swift
//  ChickTracker
//
//  Created by 김규진 on 2022/11/04.
//

import SwiftUI

struct RecentTransactionList: View {
    @EnvironmentObject var transactionListVM : TransactionListViewModel
    var body: some View {
        VStack {
            HStack {
                //MARK : Header Title
                Text("활동 분석")
                    .bold()
                
                Spacer()
            }
            .padding(.top)
            
            ForEach(Array(transactionListVM.transactions.prefix(1).enumerated()), id:\.element) { index, transaction in TransactionRow(transaction: transaction)
                
                Divider()
                    .opacity(index == 3 ? 0 : 1)
            }
        }
        .padding()
        .background(Color.systemBackground)
        .clipShape(RoundedRectangle(cornerRadius: 20, style: .continuous))
            .shadow(color: Color.primary.opacity(0.2), radius: 10, x: 0, y: 5)
    }
}

struct RecentTransactionList_Previews: PreviewProvider {
    static let transactionListVM: TransactionListViewModel = {
        let transactionListVM = TransactionListViewModel()
        transactionListVM.transactions = transactionListPreviewData
        return transactionListVM
    }()
    static var previews: some View {
        Group{
            RecentTransactionList()
            RecentTransactionList()
                .preferredColorScheme(.dark)
        }
        .environmentObject(transactionListVM)
    }
}
