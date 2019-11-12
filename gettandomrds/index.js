const mysql = require('mysql');
var con = mysql.createConnection({
    host: "database-1.cdbq6xqd24lq.us-east-1.rds.amazonaws.com",
    user: "admin",
    database: "climateai"
});
exports.handler = (event, context, callback) => {
    context.callbackWaitsForEmptyEventLoop = false;
    // TODO implement
    var response = {
        statusCode: 200,
        body: '',
    };
    console.log(event.lat);
    console.log(event.lon);
    let sql = 'SELECT month,tanom from tanoms where lat = ? and lon = ?';
    let lat = Math.round(event.lat);
    let lon = Math.round(event.lon);
    let param = [lat,lon];

    con.query(sql,param,function (err, result, fields) {
        if (err){
            response.statusCode=500;
            response.body=err;
            callback(null,response);
        } 
        response.body = result;
        callback(null,response);
    });
};
 
