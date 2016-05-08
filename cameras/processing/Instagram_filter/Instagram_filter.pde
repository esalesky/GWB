//SET UP
PImage img; //Declare variable of type PImage

void setup() {
  size(200,200); //Change size of image. 
  img = loadImage("IMG_3294.JPG"); //Image in our library
}

// CREATE IMAGE
void draw(){ 
  image(img,0,0,width,height); //Resize the image image(file name, x_origin, y_orgin, size x, size y)

// CREATE FILTER
  fill(255,255,0,60); //Fill shape with semi-transparent filter over image (R value,G value,B value, alpha/transparency)
  noStroke(); //no border
  rect(0,0,width,height); //Define shape of filter
  
}
