import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Counter App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Counter App'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  void _resetCounter() {
    setState(() {
      _counter = 0;
    });
  }
  
  Widget textSection(String text) {
    return Text(
      text,
      style: TextStyle(
        fontSize: 28,
      ),
    );
  }

  Widget commandSection() {
    
    return  Container(
      child: Row(
        mainAxisAlignment: MainAxisAlignment.center,
        children:[
          TextButton(
            onPressed: _incrementCounter, 
            child: Text(
              "Add"
            ),
          ),
          TextButton(
            onPressed: _resetCounter, 
            child: Text(
              "Reset"
            ),
          )
        ] 
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            textSection('You have pressed the button :'),
            textSection('$_counter' + " time(s)"),
            SizedBox(height: 10,),
            commandSection(),
          ],
        ),
      ),
    );
  }
}
