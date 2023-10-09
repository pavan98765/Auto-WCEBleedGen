function f_str2lab_testdata(pxds,tmpdir,fldr)

for i = 1:length(pxds.Files)
    % disp(i)
    file = readimage(pxds,i);
    nfile = zeros(size(file));
    
    nfile(file == "one") = 1;
    [~,name,ext] = fileparts(pxds.Files(i));
    imwrite(nfile, [tmpdir '\' fldr '\' name ext])
end

end