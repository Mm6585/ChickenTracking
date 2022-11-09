//
//  TransactionRow.swift
//  ChickTracker
//
//  Created by 김규진 on 2022/11/04.
//

import SwiftUI
import SwiftUIFontIcon

struct TransactionRow: View {
    var transaction : chickTrackJson
    
    var body: some View {
        VStack{
        HStack(spacing: 20){
            
            RoundedRectangle(cornerRadius: 20,style: .continuous)
                .fill(Color.icon.opacity(0.3))
                .frame(width: 44, height: 44)
                .overlay{
                    FontIcon.text(.awesome5Solid(code: .icons), fontsize: 24, color: Color.icon)
                }
            
            VStack(alignment: .leading, spacing: 6){
                // MARK: Transaciton Category
                Text("활동량")
                    .font(.subheadline)
                    .bold()
                    .lineLimit(1)
                
                // MARK: Transaciton Category
                Text("activity")
                    .font(.footnote)
                    .opacity(0.7)
                    .lineLimit(1)
                
                Text(transaction.date)
                    .font(.footnote)
                    .foregroundColor(.secondary)
            }
            Spacer()
            Text(String(floor(transaction.amountofActivity)))
                .bold()
            
        }
        .padding([.top, .bottom],8)
            
        Divider()
                .opacity(1)
        
        HStack(spacing: 20){
            
            RoundedRectangle(cornerRadius: 20,style: .continuous)
                .fill(Color.icon.opacity(0.3))
                .frame(width: 44, height: 44)
                .overlay{
                    FontIcon.text(.awesome5Solid(code: .icons), fontsize: 24, color: Color.icon)
                }
            
            VStack(alignment: .leading, spacing: 6){
                // MARK: Transaciton Category
                Text("객체수")
                    .font(.subheadline)
                    .bold()
                    .lineLimit(1)
                
                Text("individiual")
                    .font(.footnote)
                    .opacity(0.7)
                    .lineLimit(1)
                
                Text(transaction.date)
                    .font(.footnote)
                    .foregroundColor(.secondary)
            }
            Spacer()
            Text(String(transaction.objNumber))
                .bold()
        }.padding([.top, .bottom],8)
    }
    
    }
}

struct TransactionRow_Previews: PreviewProvider {
    static var previews: some View {
        Group {
            TransactionRow(transaction: transactionPreviewData)
            TransactionRow(transaction: transactionPreviewData).preferredColorScheme(.dark)
        }
    }
}
