## Server - code run through

![Fetched file contents](https://drive.google.com/file/d/1A5WVjAWp2GERXC423MrE40NX2Y7jcoJy/view?usp=sharing)

![Error 404 displayed](https://drive.google.com/file/d/1KdZEfltY8rz0TVw9DBxz899Juu3yxpFq/view?usp=sharing)

![Running server](https://drive.google.com/file/d/1brkNvGPfGRS8pmY-4TEtymyth5bleAcQ/view?usp=sharing)

The server starts by importing the necessary modules and defining a signal handler function to gracefully terminate the program on receiving a SIGINT signal. Then it creates a socket using the AF_INET and SOCK_STREAM protocols and binds it to the host's IP address and a predefined port number which is 8080 in this program.

It handles one HTTP request at a time; listens for incoming connections in a while loop, accepts a connection, processes the request, and sends a response before closing the connection.

It accepts and parses the HTTP request by receiving the message from the client, decoding it, and extracting the requested file name from the GET request line.

If the requested file is present in the server's file system, the server opens the file, reads its content, creates an HTTP response message consisting of the requested file preceded by header lines indicating the HTTP version, status code, content type, and content length. The server then sends the response directly to the client.

If the requested file is not present in the server, the server sends an HTTP “404 Not Found” message back to the client. The server generates and sends the HTTP response message with the status code and content type headers, but without any content.

In summary, the program handles one HTTP request at a time, accepts and parses the HTTP request, gets the requested file from the server's file system, creates an HTTP response message consisting of the requested file preceded by header lines, and sends the response directly to the client. If the requested file is not present in the server, the server sends an HTTP “404 Not Found” message back to the client.
