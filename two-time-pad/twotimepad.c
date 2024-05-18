#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

void xorBMP(const char *inputFile1, const char *inputFile2, const char *outputFile) {
    FILE *file1 = fopen(inputFile1, "rb");
    FILE *file2 = fopen(inputFile2, "rb");
    FILE *output = fopen(outputFile, "wb");

    if (file1 == NULL || file2 == NULL || output == NULL) {
        printf("Error opening files.\n");
        return;
    }

    // Copy BMP header from the first input file to the output file
    uint8_t header[54];
    fread(header, sizeof(uint8_t), 54, file1);
    fwrite(header, sizeof(uint8_t), 54, output);

    // Determine the size of the files
    fseek(file1, 0, SEEK_END);
    fseek(file2, 0, SEEK_END);
    long fileSize1 = ftell(file1);
    long fileSize2 = ftell(file2);
    long minSize = (fileSize1 < fileSize2) ? fileSize1 - 54 : fileSize2 - 54; // Subtract header size


    fseek(file1,54,SEEK_SET);
    fseek(file2,54,SEEK_SET);

    // XOR pixel data byte by byte
    uint8_t byte1, byte2, result;
    for (long i = 0; i < minSize; ++i) {
        fread(&byte1, sizeof(uint8_t), 1, file1);
        fread(&byte2, sizeof(uint8_t), 1, file2);
        result = byte1 ^ byte2;
        fwrite(&result, sizeof(uint8_t), 1, output);
    }

    fclose(file1);
    fclose(file2);
    fclose(output);

    printf("Images XORed successfully and saved to %s\n", outputFile);
}

int main() {
    xorBMP("enc1.bmp", "enc2.bmp", "output.bmp");
    return 0;
}

