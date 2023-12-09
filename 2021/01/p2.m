function ans = p2(inputFile)
    t = readtable(inputFile, 'ReadVariableNames', false);
    a = t.Var1;

    f = filter([1 0 0 -1], [1 -1], a);
    c = f(3:end);
    d = c(2:end) - c(1:end-1);
    ans = sum(d > 0);
end
