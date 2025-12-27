package jmods;

import java.util.*;

public class DMS {

    public static long fact(int n){
        if(n < 0) throw new IllegalArgumentException();
        long r = 1;
        for(int i=2;i<=n;i++) r *= i;
        return r;
    }

    public static Object[] convert(double value, String unit){
        unit = unit.toLowerCase();
        switch(unit){
            case "farenheit": return new Object[]{(value-32)*5/9,"Celsius"};
            case "celcius": return new Object[]{(value*9/5)+32,"Fahrenheit"};
            case "centimeters": return new Object[]{value/2.54,"Inches"};
            case "inches": return new Object[]{value*2.54,"Centimeters"};
            default: return new Object[]{null,"Error"};
        }
    }

    public static double mean(double[] d){
        if(d.length==0) return 0;
        double s=0;
        for(double x:d) s+=x;
        return s/d.length;
    }

    public static double median(double[] d){
        if(d.length==0) return 0;
        Arrays.sort(d);
        int m = d.length/2;
        return d.length%2==0 ? (d[m-1]+d[m])/2 : d[m];
    }

    public static List<Double> mode(double[] d){
        Map<Double,Integer> c = new HashMap<>();
        for(double x:d) c.put(x,c.getOrDefault(x,0)+1);
        int max = Collections.max(c.values());
        List<Double> r = new ArrayList<>();
        for(var e:c.entrySet())
            if(e.getValue()==max) r.add(e.getKey());
        return r;
    }

    public static double standardDeviation(double[] d){
        if(d.length<2) return 0;
        double avg = mean(d);
        double v=0;
        for(double x:d) v+=(x-avg)*(x-avg);
        return Math.sqrt(v/(d.length-1));
    }
}
