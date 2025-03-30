const express = require("express");
const bodyparser = require("body-parser");
require("dotenv").config();
const mongoose = require("mongoose");
const portfolioRoutes = require("./routes/portfolio");


const cors = require('cors');

const app = express();
const port = process.env.PORT;

//middleware
// app.use(cors({ origin: 'http://localhost:3000' }));
app.use(bodyparser.json());
app.use(
  bodyparser.urlencoded({
    extended: true,
  })
);

// mongoose
//   .connect(process.env.MONGO_URI)
//   .then(() => {
//     app.listen(port, () => {
//       console.log("server running at port :", port);
//     });
//   })
//   .catch((error) => {
//     console.log(error);
//   });

app.listen(port, () => {
        console.log("server running at port :", port);
      });

app.use("/api/portfolio", portfolioRoutes);
