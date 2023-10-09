
% % %  --------- renaming images and mask --------------------

clc
close all
clear all

drim = f_rem_dir(dir('D:\data\BLEEDconf\WCEBleedGen\bleeding\Images'));
drmsk = f_rem_dir(dir('D:\data\BLEEDconf\WCEBleedGen\bleeding\Annotations'));

pthim = 'D:\data\BLEEDconf\WCEBleedGen\combine\Images';
pthmsk = 'D:\data\BLEEDconf\WCEBleedGen\combine\Annotations';

parfor i = 1:length(drim)
    disp(i)
    im = imread([drim(i).folder '/' drim(i).name]);
    imwrite(im, [pthim '/' 'i_' num2str(i) '.png']);

    im = imread([drmsk(i).folder '/' drmsk(i).name]);
    imwrite(im, [pthmsk '/' 'a_' num2str(i) '.png']);
end

cnt = length(drim);

drim = f_rem_dir(dir('D:\data\BLEEDconf\WCEBleedGen\non-bleeding\Images'));
drmsk = f_rem_dir(dir('D:\data\BLEEDconf\WCEBleedGen\non-bleeding\Annotations'));

pthim = 'D:\data\BLEEDconf\WCEBleedGen\combine\Images';
pthmsk = 'D:\data\BLEEDconf\WCEBleedGen\combine\Annotations';

parfor i = 1:length(drim)
    disp(i+cnt)
    im = imread([drim(i).folder '/' drim(i).name]);
    imwrite(im, [pthim '/' 'i_' num2str(i+cnt) '.png']);

    im = imread([drmsk(i).folder '/' drmsk(i).name]);
    imwrite(im, [pthmsk '/' 'a_' num2str(i+cnt) '.png']);
end


%%% ---- some masks are in 3D format ------------------
%%% ----- converting 3d maks to 2d masks ------------------


clc
clear all
close all

pthim = 'D:\data\BLEEDconf\WCEBleedGen\non-bleeding\Images';
pthmsk = 'D:\data\BLEEDconf\WCEBleedGen\non-bleeding\Annotations';

drim = f_rem_dir(dir(pthim));
drmsk = f_rem_dir(dir(pthmsk));

cnt = 0;
for i = 1:length(drim)

    im = imread([drmsk(i).folder '/' drmsk(i).name]);
    if length(size(im)) == 3
        cnt = cnt+1;
        idx(cnt) = i;
    end
end


for i = idx
    im = imread([drmsk(i).folder '/' drmsk(i).name]);
    imwrite(im(:,:,1), [drmsk(i).folder '/' drmsk(i).name]);
end



%%% separating RGB image into R and G channels
%%% --------------------------------------------------------
clc
close all
clear all

pthim = 'D:\data\BLEEDconf\WCEBleedGen\combine\Images';
drim = f_rem_dir(dir(pthim));
ch = 1;

if ch == 1
    pthim = 'D:\data\BLEEDconf\WCEBleedGen\combine\r';
    parfor i = 1:length(drim)
        disp(num2str(i))
        im = imread([drim(i).folder '/' drim(i).name]);
        im = repmat(im(:,:,1),[1 1 3]);        
        imwrite(im, [pthim '/' drim(i).name]);
    end
end

ch = 2;
if ch == 2
    pthim = 'D:\data\BLEEDconf\WCEBleedGen\combine\g';
    parfor i = 1:length(drim)
        disp(num2str(i))
        im = imread([drim(i).folder '/' drim(i).name]);
        im = repmat(im(:,:,2),[1 1 3]);
        imwrite(im, [pthim '/' drim(i).name]);
    end
end



