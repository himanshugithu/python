#include <ESP8266WebServer.h>
#include <ESP8266WiFi.h>

WiFiClient client;
const char* ssid = "Thakkar";  // Enter SSID here 
const char* password = "8169099329"; //Enter Password here

ESP8266WebServer server(80);              
const int ledPin = D4;
void setup() {
  Serial.begin(115200);
  delay(100);
  Serial.println("Connecting to ");
  Serial.println(ssid);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
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
  server.on("/", HTTP_GET, handleRoot);
  server.on("/on", HTTP_GET, handleOn);
  server.on("/off", HTTP_GET, handleOff);
  server.begin();
  Serial.println("HTTP server started");

}
void loop() 
{
  server.handleClient();
}

void handleOn() {
  digitalWrite(ledPin, HIGH);
  server.send(200, "text/plain", "LED turned on");
}

void handleOff() {
  digitalWrite(ledPin, LOW);
  server.send(200, "text/plain", "LED turned off");
}


int i = 1;
void handle_OnConnect() {
  i++;
  server.send(200, "text/html", SendHTML(i)); 
  
}

void handle_NotFound(){
  server.send(404, "text/plain", "Not found");
}
String SendHTML(int data){
  String ptr = (String)data;
  return ptr;
}
void handleRoot() {
  String html = "<html><body>";
  html += "<h1>LED Control</h1>";
  html += "<p><a href='/on'><button>Turn On</button></a></p>";
  html += "<p><a href='/off'><button>Turn Off</button></a></p>";
  html += "</body></html>";

  server.send(200, "text/html", html);
}