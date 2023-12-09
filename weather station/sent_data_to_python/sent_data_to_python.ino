#include <ESP8266WebServer.h>
/*Put your SSID & Password*/
const char* ssid = "Thakkar";  // Enter SSID here 
const char* password = "8169099329"; //Enter Password here

ESP8266WebServer server(80);              
 
void setup() {
  Serial.begin(115200);
  delay(100);
  Serial.println("Connecting to ");
  Serial.println(ssid);

  //connect to your local wi-fi network
  WiFi.begin(ssid, password);

  //check wi-fi is connected to wi-fi network
  while (WiFi.status() != WL_CONNECTED) {
  delay(1000);
  Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected..!");
  Serial.print("Got IP: ");  Serial.println(WiFi.localIP());

  server.on("/", handle_OnConnect);
  server.onNotFound(handle_NotFound);

  server.begin();
  Serial.println("HTTP server started");

}
void loop() {
  server.handleClient();
}

void handle_OnConnect() {
 String data = "Hello from esp";
  server.send(200, "text/html", SendHTML(data)); 
}

void handle_NotFound(){
  server.send(404, "text/plain", "Not found");
}
String SendHTML(String data){
  String ptr = data;
  return ptr;
}
