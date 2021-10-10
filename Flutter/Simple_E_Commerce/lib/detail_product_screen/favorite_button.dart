import 'package:flutter/material.dart';

class FavoriteButton extends StatefulWidget{
  
  @override
  _FavoriteButtonState createState() => _FavoriteButtonState();
}

class _FavoriteButtonState extends State<FavoriteButton> {
  bool _isFavorite = false;

  @override
  Widget build(BuildContext context){
    return IconButton(
      onPressed: (){
        setState( () {
          _isFavorite = !_isFavorite;
        });
      },
      icon: Icon(
        _isFavorite ? Icons.favorite : Icons.favorite_border,
        color: Color(0xffDA0037),
      ),
    );
  }
}