class Main
{
	constructor()
	{
		Main.instance = this;
		this.Field = new Field();
		this.Tile = new Tile();
	}

	getMainNode()
	{
		if (this.mainNode === undefined) {
			this.mainNode = document.getElementById('main');
		}
		return this.mainNode;
	}
	
	getFieldNode()
	{
		return this.Field.getNode();
	}

	getTileNode()
	{
		return this.Tile.getNode();
	}
}

class Field
{
	constructor()
	{

	}
}

class Tile
{
	constructor()
	{

	}
}
