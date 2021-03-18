package com.yikliu.leetcode.problems;

import java.util.Optional;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class EditDistanceTest {

    private EditDistance editDistance;

    @BeforeEach
    public void setup(){
       editDistance = new EditDistance();
    }

    @Test
    public void testEditDistance() {
        Assertions.assertEquals(3, editDistance.minEditDistance("horse", "ros"));
        Assertions.assertEquals(0, editDistance.minEditDistance("", ""));
        Assertions.assertEquals(5, editDistance.minEditDistance("intention", "execution"));
    }
}

