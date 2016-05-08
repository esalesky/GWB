PImage img; //Declare variable of type PImage
PImage solid_color = createImage(200, 200,RGB); //Solid color overlay

void setup() {
  size(200,200); //Change size of image. 
  img = loadImage("IMG_3294.JPG"); //Image in our library
}

void draw(){ 
  background(0);
  //Draw the image to the screen at coordinate (0,0)
//  tint(220,220,255); //3 arguments represent Red green and blue 0-->255 intensity values. 
  //background(solid_color);
  image(img,0,0,width,height); //Resize the image image(file name, x_origin, y_orgin, size x, size y)

  fill(255,255,0,60); //Fill shape with semi-transparent filter over image (R value,G value,B value, alpha/transparency)
  noStroke(); //no border
  rect(0,0,width,height); //Define shape of filter
  
}