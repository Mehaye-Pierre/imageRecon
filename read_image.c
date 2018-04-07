#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "rdjpeg.h"

#define RBINS 4
#define GBINS 4
#define BBINS 4

int read_image_and_print_histogram(CIMAGE cim){

  float rgb[RBINS][GBINS][BBINS];

  for(int i = 0; i < 4; i++){
    for(int j = 0; j < 4; j++){
      for(int k = 0; k < 4; k++){
        rgb[i][j][k] = 0;
      }
    }
  }

  for(int i = 0; i < cim.nx; i++){
    for(int j = 0; j < cim.ny; j++){
      int r = (cim.r[i][j] * RBINS) / 256;
      int g = (cim.g[i][j] * GBINS) / 256;
      int b = (cim.b[i][j] * BBINS) / 256;

      rgb[r][g][b]++;
    }
  }

  for(int i = 0; i < 4; i++){
    for(int j = 0; j < 4; j++){
      for(int k = 0; k < 4; k++){
        rgb[i][j][k] /= (cim.nx * cim.ny);
      }
    }
  }

  int compteur = 1;
  printf("0 ");
  for(int k = 0; k < 4; k++){
	for(int j = 0; j < 4; j++){
	  for(int i = 0; i < 4; i++){
		if (rgb[i][j][k] > 0.0) printf("%d:%lf ", compteur, rgb[i][j][k]);
		compteur++;
	  }
	}
  }
  printf("\n");
}


int main(int argc, char *argv[])
{
  CIMAGE cim;
  read_cimage(argv[1],&cim);
  read_image_and_print_histogram(cim);
  exit(0);
}
