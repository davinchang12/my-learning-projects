import 'package:flutter/material.dart';

import 'package:submission_dicoding/product/product_data.dart';
import 'package:submission_dicoding/detail_product_screen/detail_product.dart';

import 'package:flutter_rating_bar/flutter_rating_bar.dart';

class MainScreenItems extends StatelessWidget{
  
  final ProductData product = ProductData.productDataList;

  @override
  Widget build(BuildContext context){
    return Expanded(
      child: ListView(
        padding: EdgeInsets.all(25),
        shrinkWrap: true,
        children: List.generate(
          10, 
          (index) => GestureDetector(
            onTap: () {
              Navigator.push(context, MaterialPageRoute(builder: (context){
                return DetailProduct(index: (index + 1));
              }));
            },
            child: Container(
              padding: EdgeInsets.only(
                left: 5,
                right: 5,
              ),
              margin: EdgeInsets.only(
                bottom: 20
              ),
              child: Card(
                shadowColor: Colors.black,
                elevation:50,
                color: Color(0xff444444),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(10)
                ),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.start,
                  children: [ 
                    Flexible(
                      child: ClipRRect(
                        borderRadius: BorderRadius.only(
                          topLeft: Radius.circular(10),
                          bottomLeft: Radius.circular(10),
                        ),
                        child: Image.asset(
                          product.image,
                          height: 130,
                          width: 160,
                          fit: BoxFit.fitHeight,
                        ),
                      ),
                    ),
                    Flexible(
                      child: Container(
                        padding: const EdgeInsets.only(
                          left: 12,
                          right: 12,
                        ),
                        child: Column(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [ 
                            Text(
                              ("(" + (index + 1).toString() + ") " + product.name),
                              style: TextStyle(
                                color: Color(0xffEDEDED),
                                fontSize: 12,
                                fontFamily: "Montserrat-Medium"
                              ),
                            ),

                            SizedBox(height: 12,),

                            Text(
                              product.price,
                              style: TextStyle(
                                fontWeight: FontWeight.bold,
                                color: Color(0xffEDEDED),
                                fontFamily: "Montserrat-Medium"
                              ),
                            ),

                            SizedBox(height: 12,),

                            Row(
                              mainAxisAlignment: MainAxisAlignment.spaceBetween,
                              children: [
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

                                Text(
                                  product.rating.toString(),
                                  style: TextStyle(
                                    color: Color(0xffEDEDED), 
                                    fontFamily: "Montserrat-Medium"
                                  ),  
                                ),
                              ],
                            ),
                          ],
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}