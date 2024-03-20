import 'dart:async';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(MaterialApp(
    debugShowCheckedModeBanner: false,
    home: HomePage(),
  ));
}

class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  bool enabled = true;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.blue,
        iconTheme: IconThemeData(color: Colors.white),
      ),
      drawer: Drawer(),
      body: Container(
        color: Colors.blue,
        child: Center(
          child: ElevatedButton(
            onPressed: enabled
                ? () {
                    activateSOS();
                    setState(() {
                      enabled = false;
                    });
                    startCooldown();
                  }
                : null,
            child: Text(
              'SOS',
              style: TextStyle(
                fontWeight: FontWeight.bold,
                fontSize: 100,
                color: Colors.blue,
              ),
            ),
            style: ElevatedButton.styleFrom(
              shape: CircleBorder(),
              padding: EdgeInsets.all(100),
            ),
          ),
        ),
      ),
    );
  }

  Future<void> activateSOS() async {
    try {
      final response = await http.post(
        Uri.parse('http://127.0.0.1:9999/activate_sos'),
      );

      if (response.statusCode == 200) {
        print('SOS activation successful');
      } else {
        print('Failed to activate SOS. Status code: ${response.statusCode}');
        print('Response body: ${response.body}');
      }
    } catch (error) {
      print('Error: $error');
    }
  }

  void startCooldown() {
    Timer(
      const Duration(seconds: 15),
      () => setState(() {
        enabled = true;
      }),
    );
  }
  
}
