import 'package:flutter/material.dart';

class TambahKeranjangButton extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    return MaterialButton(
      color: Color(0xffDA0037),
      textColor: Color(0xffEDEDED),
      onPressed: () {
        final snackBar = SnackBar(
          content: Text('Berhasil ditambahkan'),
          duration: Duration(seconds: 1),
        );

        ScaffoldMessenger.of(context).showSnackBar(snackBar);
      },
      child: Padding(
        padding: EdgeInsets.all(10),
        child: Text(
          "Tambah ke Keranjang",
          style: TextStyle(
            fontFamily: "Montserrat-Medium",
          ),
        ),
      ),
    );
  }
}