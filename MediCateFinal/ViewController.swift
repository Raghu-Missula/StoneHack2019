//
//  ViewController.swift
//  MediCateFinal
//
//  Created by Varun Giridhar on 3/22/19.
//  Copyright © 2019 Varun Giridhar. All rights reserved.
//

import UIKit
import Firebase
import FirebaseDatabase
class ViewController: UIViewController{
    
    var ref: DatabaseReference!

    
    override func viewDidLoad() {
        super.viewDidLoad()
        writeData()
    }
    func writeData(){
        ref = Database.database().reference()
        self.ref.child("users").setValue("hello world!")

    }
    @IBAction func takePhoto(_ sender: Any) {
        
    }
    
}

