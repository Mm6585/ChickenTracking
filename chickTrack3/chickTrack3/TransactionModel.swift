//
//  TransactionModel.swift
//  chickTrack3
//
//  Created by 김규진 on 2022/11/08.
//

import Foundation


struct chickTrackJson : Identifiable,Decodable,Hashable {
    let id: Int
    let date : String
    let objNumber : Int
    let amountofActivity : Double
    var dateParsed : Date {
        date.dateParsed()
    }
    
}



