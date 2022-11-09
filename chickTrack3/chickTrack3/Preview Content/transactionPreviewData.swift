//
//  PreviewData.swift
//  ChickTracker
//
//  Created by 김규진 on 2022/11/04.
//

import Foundation

var transactionPreviewData = chickTrackJson(id:1, date: "20221106", objNumber: 15, amountofActivity: 3030)

var transactionListPreviewData = [chickTrackJson](repeating: transactionPreviewData, count: 10)

