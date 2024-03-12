from http.server import HTTPServer,BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title>SOFTWARE COMPANIES WITH REVENUE</title> 
    </head>

    <body>
        <center>
            <h3>TOP FIVE SOFTWARE COMPANIES</h3>
        
        <table border="4" cellspacing="5">
               <tr>
                  <th>Rank</th>
                  <th>Company Name</th>
                  <th>Revenue</th>
                </tr>

                <tr>
                  <td>1</td>
                  <td>Apple</td>
                  <td>$385.70</td>
                <tr>

                </tr>
                  <td>2</td>
                  <td>Google</td>
                  <td>$307.39 B </td>
                </tr>

                <tr>    
                   <td>3</td>
                   <td>Microscoft</td>
                   <td>$227.58 B</td>
                </tr>    
                
                </tr>
                   <td>4</td>
                   <td>IBM</td>
                   <td>$61.85 B </td>
                </tr>
                <tr>
                   <td>5</td>
                   <td>Oracle</td>
                   <td>$51.62 B</td>
                </tr>

        </table>
        <center>
            
        </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()