const { spawn } = require("child_process");

const portfolioController = async (req,res) => {
    const args = req.body.tickers;
    const option = req.body.option;
    console.log(...args)
    if(option>3 || option<1) res.status(200).json({mssg:"Please Select a option : 1.Minimum Volatility Portfolio 2.Max Return Portfolio 3.Optimal Portfolio"})
    var output="";
    const childPython = spawn("python" , ["./controllers/calculations/calculation.py",...args])
    childPython.stdout.on('data', (data)=>{
        output+=data.toString();
        console.log(data);
    })
    childPython.stderr.on('data', (error) => {
        console.error(error.toString());
    });
    childPython.on('close',(code)=>{
        if(code===0){
            const lines = output.split('\n');
            console.log(lines)
            const minVolPort = JSON.parse(lines[0]);
            const maxRetPort = JSON.parse(lines[1]);
            const optimalPort = JSON.parse(lines[2]);
            // console.log('Minimum Volatility Portfolio:', minVolPort);
    // console.log('Maximum Return Portfolio:', maxRetPort);
    // console.log('Optimal Portfolio Based on Sharpe Ratio:', optimalPort);
    if(option===1) output=minVolPort
    else if (option===2) output=maxRetPort
    else output=optimalPort
    res.status(200).json({portfolio:output})
        }
        else{
            console.error(`Python script exited with code ${code}`);
            res.status(401).json({error:"Python script failed"})
        }
    })
}

module.exports={
    portfolioController
} 

// {
//     Returns: 0.5158337984117553,
//     Volatility: 0.5372568838394925,
//     'GOOG weight': 0.0225024466633707,
//     'F weight': 0.014469582033826622,
//     'WMT weight': 0.026751821270756544,
//     'TSLA weight': 0.9362761500320461
//   }