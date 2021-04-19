clc;
clear;

files = dir("../test_images/*.png");

for loop = 1:numel(files)
    filename = files(loop).name;
    input_image = imread(fullfile("../test_images/",filename));
    
    if(size(input_image,3)==3)
     input_image = uint8(input_image);
     input_image = rgb2gray(input_image);
    end

    input_image = double(input_image);


    feat = brisque_feature(input_image);
    
    disp(['BRISQUE features computed for ',filename]);
    
    disp(feat);
end
