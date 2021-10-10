import 'package:flutter/material.dart';


class MainScreenHeader extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    return Container(
      child: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  IconButton(
                    onPressed: (){}, 
                    icon: Icon(
                      Icons.person,
                      color: Color(0xffDA0037),
                    ),
                    iconSize: 28,
                  ),
                  Text(
                    "E-commerence",
                    style: TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                      color: Color(0xffEDEDED),
                      fontFamily: "Montserrat-Medium",
                    ),
                  ),
                  IconButton(
                    onPressed: () {}, 
                    icon: Icon(
                      Icons.backpack,
                      color: Color(0xffDA0037),
                    ),
                    iconSize : 28
                  )
                ],
              ),

              SizedBox(height: 20.0),
            
              TextField(
                decoration: InputDecoration(
                  border: new OutlineInputBorder(
                    borderSide: new BorderSide(color: Colors.teal),
                  ),
                  fillColor: Color(0xff444444),
                  filled: true,
                  
                  labelText: 'Search',
                  labelStyle: TextStyle(
                    color: Color(0xffEDEDED)
                  ),

                  suffixIcon: Icon(
                    Icons.search,
                    color: Color(0xffDA0037)
                  ),

                ),
                onChanged: (String value) {

                },
              ),
              SizedBox(height: 28.0),       
            ],
          ),
        ),
      ),
    );
  }
}
