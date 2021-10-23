class Item {
  String id;
  String name;
  int price;

  Item(this.id, this.name, this.price);

  List<Item> itemShop = [
    Item("1", "Item 1", 100),
    Item("2", "Item 2", 100),
    Item("3", "Item 3", 100),
    Item("4", "Item 4", 100),
    Item("5", "Item 5", 100),
    Item("6", "Item 6", 100)
  ];
}