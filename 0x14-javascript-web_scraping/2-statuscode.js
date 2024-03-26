#!/usr/bin/node
const request = require('request');

function getStatusCode(url) {
	    request.get(url, (error, response) => {
		            if (error) {
				                console.error(`Error: ${error.message}`);
				            } else {
						                console.log(`code: ${response.statusCode}`);
						            }
		        });
}

if (process.argv.length !== 3) {
	    console.error('Usage: node script.js <URL>');
	    process.exit(1);
}

const url = process.argv[2];
getStatusCode(url);
