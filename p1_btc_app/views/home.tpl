<html>
          <head>
                    <title> BTC App </title>
                    <style> 
                            * {
                                   font-size: 50px;
                                   text-align:center;
                            
                            }
                            body {
                                   background-color:lightcyan;
                            }
                            .fc {
                                   border: solid;
                                   width:60%;
                                   margin:auto;
                                   padding:1%;
                                   border-radius:30px;
                            }
                     </style>
          </head>
          <body>
                     <h1>BTC App</h1>
                     <div class="fc">
                     <form method = "POST">
                           <input type="number"
                                   name="noc"
                                   placeholder="Enter Number of Coins"
                                   required
                                   min="1"
                      />
                      <br/><br/>
                      <input type="submit"
                               value="Find Price"
                           />
                     </form>    
                     </div>
                     <h2>
                           {{ msg }}
                     </h2>
          </body>
</html>



 