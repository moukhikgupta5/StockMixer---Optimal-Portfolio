const express = require('express')

const {portfolioController} = require('../controllers/portfolioController')

const router = express.Router();

router.post("/", portfolioController);

module.exports = router;