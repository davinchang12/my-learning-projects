import 'package:flutter/material.dart';
import 'package:submission_dicoding/product/product_data.dart';

class SizeButton extends StatefulWidget{

  final ProductData product;

  SizeButton({required this.product});

  @override
  _SizeButtonState createState() => _SizeButtonState();
}

class _SizeButtonState extends State<SizeButton> {
  
  int _curr = 0;

  @override
  Widget build(BuildContext context){
    return Row(
      children: widget.product.size.map( (size) {
        int index = widget.product.size.indexOf(size);
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
            child: sizeSelected(context, size, _curr == index)
          ),
        );
      }).toList(),
    );
  }

  Widget sizeSelected(BuildContext context, String size, bool selected){
    return Container(
      width: 30,
      height: 30,
      decoration: BoxDecoration(
        color: selected ? Color(0xffDA0037) : Color(0xff444444),
        boxShadow: [
          BoxShadow(
            color: selected ? Colors.black : Color(0xff171717),
            blurRadius: 8,
            offset: Offset(4, 4),
          ),
        ],
      ),
      child: Padding(
        padding: EdgeInsets.only(
          top: 10,
        ),
        child: Text(
          size,
          style: TextStyle(
            color: Color(0xffEDEDED),
            fontSize: 10,
            fontFamily: "Montserrat-Medium",
          ),
          textAlign: TextAlign.center,
        ),
      ),
    );
  }
}