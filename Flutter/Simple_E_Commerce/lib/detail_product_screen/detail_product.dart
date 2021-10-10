import 'package:flutter/material.dart';
import 'package:submission_dicoding/detail_product_screen/favorite_button.dart';
import 'package:submission_dicoding/detail_product_screen/jumlah_button.dart';
import 'package:submission_dicoding/detail_product_screen/tambah_keranjang_button.dart';
import 'package:submission_dicoding/detail_product_screen/warna_button.dart';

import 'package:submission_dicoding/product/product_data.dart';
import 'package:flutter_rating_bar/flutter_rating_bar.dart';
import 'package:submission_dicoding/detail_product_screen/size_button.dart';

class DetailProduct extends StatelessWidget{

  final int index;
  final ProductData product = ProductData.productDataList;
  
  DetailProduct({required this.index});

  @override
  Widget build(BuildContext context){
    return Scaffold(
      body: SafeArea(
        child: SingleChildScrollView(
          child: Column(
            children: [
              Padding(
                padding: EdgeInsets.all(20),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    IconButton(
                      onPressed: () {
                        Navigator.pop(context);
                      },
                      icon: Icon(
                        Icons.arrow_back,
                        color: Color(0xffDA0037),
                      ),
                    ),
                    FavoriteButton(),
                  ],
                ),
              ),

              Container(
                alignment: Alignment.center,
                child: Padding(
                  padding: EdgeInsets.only(
                    left: 20,
                    right: 20,
                    bottom: 20,
                  ),
                  child: ClipRRect(
                    borderRadius: BorderRadius.circular(8),
                    child: Image.asset(
                      product.image,
                      width: 450,
                    ),
                  ),
                ),
              ),

              Container(
                padding: EdgeInsets.only(
                  left: 20,
                  right: 20,
                ),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Flexible(
                      child : Text(
                        ("(" + (index).toString() + ") " + product.name),
                        style: TextStyle(
                          color: Color(0xffEDEDED),
                          fontSize: 20,
                          fontFamily: "Montserrat-Medium",
                        ),
                        overflow: TextOverflow.ellipsis,
                      ),
                    ),

                    RatingBar.builder(
                      initialRating: product.rating,
                      ignoreGestures: true,
                      minRating: 1,
                      direction: Axis.horizontal,
                      allowHalfRating: true,
                      itemCount: 5,
                      itemPadding: EdgeInsets.symmetric(horizontal: 4.0),
                      itemSize: 12,
                      itemBuilder: (context, _) => Icon(
                        Icons.star,
                        color: Colors.amber,
                      ),
                      onRatingUpdate: (rating) {
                        print(rating);
                      },
                    ),
                  ],
                ),
              ),

              SizedBox(height: 20,),

              Padding(padding: EdgeInsets.only(
                left: 20,
                right: 20,
              ),
                child: Align(
                  alignment: Alignment.centerLeft,
                  child: Text(
                    "Deskripsi Produk",
                    style: TextStyle(
                      color: Color(0xff444444),
                      fontWeight: FontWeight.bold,
                      fontFamily: "Montserrat-Medium",
                    ),
                    textAlign: TextAlign.left,
                  ),
                ),
              ),

              Container(
                padding: EdgeInsets.only(
                  left: 20,
                  right: 20,
                  top: 10,
                ),
                child: Text(
                  product.desc,
                  style: TextStyle(
                    color: Color(0xffEDEDED),
                    fontFamily: "Montserrat-Medium",
                  ),
                  maxLines: 3,
                  overflow: TextOverflow.ellipsis,
                ),
              ), 

              SizedBox(height: 20,),

              Padding(padding: EdgeInsets.only(
                left: 20,
                right: 20,
              ),
                child: Align(
                  alignment: Alignment.centerLeft,
                  child: Text(
                    "Warna",
                    style: TextStyle(
                      color: Color(0xff444444),
                      fontWeight: FontWeight.bold,
                      fontFamily: "Montserrat-Medium",
                    ),
                    textAlign: TextAlign.left,
                  ),
                ),
              ),
              
              WarnaButton(product: product),

              SizedBox(height: 20,),

              Padding(padding: EdgeInsets.only(
                left: 20,
                right: 20,
              ),
                child: Align(
                  alignment: Alignment.centerLeft,
                  child: Text(
                    "Ukuran",
                    style: TextStyle(
                      color: Color(0xff444444),
                      fontWeight: FontWeight.bold,
                      fontFamily: "Montserrat-Medium",
                    ),
                    textAlign: TextAlign.left,
                  ),
                ),
              ),
              
              SizeButton(product: product),

              SizedBox(height: 20,),

              Padding(padding: EdgeInsets.only(
                left: 20,
                right: 20,
              ),
                child: Align(
                  alignment: Alignment.centerLeft,
                  child: Text(
                    "Jumlah",
                    style: TextStyle(
                      color: Color(0xff444444),
                      fontWeight: FontWeight.bold,
                      fontFamily: "Montserrat-Medium",
                    ),
                    textAlign: TextAlign.left,
                  ),
                ),
              ),

              JumlahButton(),

              SizedBox(height: 20,),

              Padding(padding: EdgeInsets.only(
                left: 20,
                right: 20,
              ),
                child: Align(
                  alignment: Alignment.centerLeft,
                  child: Text(
                    "Harga",
                    style: TextStyle(
                      color: Color(0xff444444),
                      fontWeight: FontWeight.bold,
                      fontFamily: "Montserrat-Medium",
                    ),
                    textAlign: TextAlign.left,
                  ),
                ),
              ),

              Padding(
                padding: EdgeInsets.only(
                  left: 20,
                  right: 20,
                  top: 10,
                ),
                child: Align(
                  alignment: Alignment.centerLeft,
                  child: Text(
                    product.price,
                    style: TextStyle(
                      color: Color(0xffEDEDED),
                      fontWeight: FontWeight.bold,
                      fontSize: 24,
                      fontFamily: "Montserrat-Medium",
                    ),
                    textAlign: TextAlign.left,
                  ),
                ),
              ),

              SizedBox(height: 20,),

              TambahKeranjangButton(),
            ],
          ),
        ),
      ),
    );
  }
}







