import 'package:flutter/material.dart';

class JumlahButton extends StatefulWidget{

  @override
  _JumlahButtonState createState() => _JumlahButtonState();
}

class _JumlahButtonState extends State<JumlahButton> {
  int _jumlah = 1;

  @override
  Widget build(BuildContext context){
    return Row(
      children: [
        Padding(
          padding: EdgeInsets.only(
            left: 20,
            top: 10,
          ),
          child: GestureDetector(
            onTap: () {
              setState( () {
                if(_jumlah > 1){
                  _jumlah--;
                }
              });
            },
            child: Container(
              width: 30,
              height: 30,
              color: Color(0xff444444),
              child: Padding(
                padding: EdgeInsets.only(
                  top: 10,
                ),
                child: Text(
                  "-",
                  style: TextStyle(
                    color: Color(0xffEDEDED),
                    fontSize: 10,
                  ),
                  textAlign: TextAlign.center,
                ),
              ),
            ),
          ),
        ),

        Padding(
          padding: EdgeInsets.only(
            left: 20,
            top: 10,
          ),
          child: Container(
            width: 30,
            height: 30,
            color: Color(0xff444444),
            child: Padding(
              padding: EdgeInsets.only(
                top: 10,
              ),
              child: Text(
                _jumlah.toString(),
                style: TextStyle(
                  color: Color(0xffEDEDED),
                  fontSize: 10,
                  fontFamily: "Montserrat-Medium",
                ),
                textAlign: TextAlign.center,
              ),
            ),
          ),
        ),

        Padding(
          padding: EdgeInsets.only(
            left: 20,
            top: 10,
          ),
          child: GestureDetector(
            onTap: () {
              setState(() {
                _jumlah++;
              });
            },
            child: Container(
              width: 30,
              height: 30,
              color: Color(0xff444444),
              child: Padding(
                padding: EdgeInsets.only(
                  top: 10,
                ),
                child: Text(
                  "+",
                  style: TextStyle(
                    color: Color(0xffEDEDED),
                    fontSize: 10,
                  ),
                  textAlign: TextAlign.center,
                ),
              ),
            ),
          ),
        ),
      ],
    );
  }
}