package com.yikliu.leetcode.problems;

import org.testng.Assert;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

public class EditDistanceTest {

    private EditDistance editDistance;

    @BeforeMethod
    public void setup(){
       editDistance = new EditDistance();
    }

    @Test
    public void testEditDistance() {
        Assert.assertEquals(2, editDistance.minEditDistance("horse", "ros"));
        Assert.assertEquals(0, editDistance.minEditDistance("", ""));
        Assert.assertEquals(5, editDistance.minEditDistance("intention", "execution"));
    }
}
