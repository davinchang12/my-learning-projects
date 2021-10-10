import 'package:flutter/material.dart';
import 'package:submission_dicoding/product/product_data.dart';

class WarnaButton extends StatefulWidget{

  final ProductData product;

  WarnaButton({required this.product});

  @override
  _WarnaButtonState createState() => _WarnaButtonState();
}

class _WarnaButtonState extends State<WarnaButton> {
  
  int _curr = 0;
  
  @override
  Widget build(BuildContext context){
    return Row(
      children: widget.product.warna.map( (warna) {
        int index = widget.product.warna.indexOf(warna);
        return Padding(
          padding: EdgeInsets.only(
            left: 20,
            top: 10,
          ),
          child: GestureDetector( 
            onTap: () {
              setState(() {
                _curr = index;
              });
            },
            child: selectedWarna(context, warna, _curr == index),
          ),
        );
      }).toList(),
    );
  }

  Widget selectedWarna(BuildContext context, Color warna, bool selected){

    return Container(
      width: 30,
      height: 30,
      decoration: BoxDecoration(
        color: warna,
        border: Border.all(
          color: Color(0xff444444),
          width: 2
        ),
        borderRadius: BorderRadius.circular(20),
        boxShadow: [
          BoxShadow(
            color: selected ? Colors.black : Color(0xff171717),
            blurRadius: 8,
            offset: Offset(4, 4),
          )
        ]
      ),
    );
  } 
}