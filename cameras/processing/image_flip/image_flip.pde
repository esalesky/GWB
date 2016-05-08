//SET UP
PImage img, img_flip;
boolean flip;

void setup() {
  size(750, 750);
  img = loadImage("spaceship.png");
  img_flip = createImage(750, 750, RGB);
  
  img.loadPixels(); //  Loads the pixel data for the image into its pixels[] array. This function must always be called before reading from or writing to pixels
  img_flip.loadPixels();
  //Save the flipped image
  for (int i = 0; i < img.width; i++) { //i++ is iterating through the pixels horizontally
    for (int j = 0; j < img.height; j++) {
      img_flip.set(i, img_flip.height-1-j, img.get(i, j));//Reads the color of the specified pixel
    }
  }
  
  img_flip.updatePixels();
  
  flip = false;
}
//DISPLAY IMAGE 
void draw() {
  background(0);
  
  if (flip) {
    image(img_flip,0,0);
  }
  else {
    image(img,0,0);
  }
}

//CONDITION FOR MOUSE CLICK (USER INPUT)
void mouseClicked() {
  flip = !flip;
}
