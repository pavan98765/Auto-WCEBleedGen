function [dr] = f_rem_dir(dr)

indx = [];
for i = 1:length(dr)
    if(dr(i).isdir == 1)
        indx = [indx i];
    end
end
dr(indx) = [];

end

