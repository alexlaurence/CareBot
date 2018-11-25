exports.handler = (event, context, callback) => {
    var seekHelp_q1 = event.currentIntent.slots.qone;
    var seekHelp_q2 = event.currentIntent.slots.qtwo;
    var seekHelp_q3 = event.currentIntent.slots.qthree;
    var seekHelp_q4 = event.currentIntent.slots.qfour;
    var seekHelp_q5 = event.currentIntent.slots.qfive;
    var total_seekHelp = seekHelp_q1 + seekHelp_q2 + seekHelp_q3 + seekHelp_q4 + seekHelp_q5;
    
    var suicide_q1 = event.currentIntent.slots.qsuione;
    var suicide_q2 = event.currentIntent.slots.qsuitwo;
    var suicide_q3 = event.currentIntent.slots.qsuithree;
    var suicide_q4 = event.currentIntent.slots.qsuifour;
    var suicide_q5 = event.currentIntent.slots.qsuifive;
    var total_suicide = suicide_q1 + suicide_q2 + suicide_q3 + suicide_q4 + suicide_q5;
    
    
    if(seekHelp_q1 == "yes")
    {
        seekHelp_q1 = 1;
    }
    else if (seekHelp_q1 == "no")
    {
         seekHelp_q1 = 0;
    }
    
    if(seekHelp_q2 == "yes")
    {
        seekHelp_q2 = 1;
    }
    else if (seekHelp_q2 == "no")
    {
         seekHelp_q2 = 0;
    }
    
    if(seekHelp_q3 == "yes")
    {
        seekHelp_q3 = 1;
    }
    else if (seekHelp_q3 == "no")
    {
         seekHelp_q3 = 0;
    }
    
    if(seekHelp_q4 == "yes")
    {
        seekHelp_q4 = 1;
    }
    else if (seekHelp_q4 == "no")
    {
         seekHelp_q4 = 0;
    }
    
    if(seekHelp_q5 == "yes")
    {
        seekHelp_q5 = 1;
    }
    else if (seekHelp_q5 == "no")
    {
         seekHelp_q5 = 0;
    }

    if (total_seekHelp >= 3)
    {
        callback(null, {
                "dialogAction": 
                {
                    "type": "Close",
                    "fulfillmentState": "Fulfilled",
                    "message": 
                    {
                    "contentType": "PlainText",
                    "content": "Let's get some help."
                    }
                }
            }); 
    }
    else 
    {
        callback(null, {
                "dialogAction": 
                {
                    "type": "Close",
                    "fulfillmentState": "Fulfilled",
                    "message": 
                    {
                    "contentType": "PlainText",
                    "content": "You'll be fine."
                    }
                }
            }); 
    }
    
    if (total_suicide >= 20)
    {
        callback(null, 
            {
                "dialogAction": 
                {
                    "type": "Close",
                    "fulfillmentState": "Fulfilled",
                    "message": 
                    {
                    "contentType": "PlainText",
                    "content": "Sending help..."
                    }
                }
        
            }); 
    }
    else 
    {
        callback(null, 
            {
                "dialogAction": 
                {
                    "type": "Close",
                    "fulfillmentState": "Fulfilled",
                    "message": 
                    {
                    "contentType": "PlainText",
                    "content": "You'll should probably seek help."
                    }
                }
        
            }); 
    }
};
