
PImage img;
boolean single_color;
//SET UP
void setup() {
  size(750, 500);
  img = loadImage("flowers.jpg");
  colorMode(HSB);
  single_color = false;
}
// DISPLAY IMAGE
void draw() {
  background(0);
  image(img, 0, 0);
}
// CHANGE TO SINGLE COLOR WHEN MOUSE IS CLICKED
void mouseClicked() {
  single_color = !single_color;
  if (single_color) {
  float h = hue(get(mouseX, mouseY));
  img.loadPixels();
  
  for (int i = 0; i < img.width; i++) {
    for (int j = 0; j < img.height; j++) {
      color c = img.get(i,j);
      float ph = hue(c);
      if (abs(ph - h) > 10.) {
        img.set(i, j, color(hue(c), 0, brightness(c)));
      }
    }
  }
  img.updatePixels();
  }
  else {
    img = loadImage("flowers.jpg");
  }
}