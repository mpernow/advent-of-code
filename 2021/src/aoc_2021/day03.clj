(ns aoc-2021.day03
  (:require [clojure.string :as str]))

(defn read-binary [s]
  (read-string (str "2r" s)))

(defn parse-numbers [input]
  (->> (slurp input)
       (str/split-lines)
       (map read-binary)))

(defn most-significant-bit [nums]
  (let [n (apply max nums)]
    (int (/ (Math/log n) (Math/log 2)))))

(defn bit-diff [nums bit]
  (reduce #(if (bit-test %2 bit) (inc %1) (dec %1))
          0
          nums))

(defn most-common-bit [nums bit] (if (neg-int? (bit-diff nums bit)) 0 1))
(defn least-common-bit [nums bit] (if (neg-int? (bit-diff nums bit)) 1 0))

(defn range-down-from [n] (range n -1 -1))

(defn gamma-rate [nums]
  (->> (range-down-from (most-significant-bit nums))
       (map (partial most-common-bit nums))
       (apply str)
       read-binary))

(defn epsilon-rate [nums]
  (->> (range-down-from (most-significant-bit nums))
       (map (partial least-common-bit nums))
       (apply str)
       read-binary))

(defn oxygen-generator-rating [nums]
  (loop [remaining nums, bit (most-significant-bit nums)]
    (if (= 1 (count remaining))
      (-> remaining first)
      (let [test (= 1 (most-common-bit remaining bit))]
        (recur (filter #(= test (bit-test % bit)) remaining)
               (dec bit))))))

(defn co2-scrubber-rating [nums]
  (loop [remaining nums, bit (most-significant-bit nums)]
    (if (= 1 (count remaining))
      (-> remaining first)
      (let [test (= 1 (least-common-bit remaining bit))]
        (recur (filter #(= test (bit-test % bit)) remaining)
               (dec bit))))))

(defn part1 [input_file]
  (->> (parse-numbers input_file)
       ((juxt gamma-rate epsilon-rate))
       (apply *)))

(defn part2 [input_file]
  (->> (parse-numbers input_file)
       ((juxt oxygen-generator-rating co2-scrubber-rating))
       (apply *)))

(defn -main []
  (let [input-file "./input/day03"]
    (println (part1 input-file))
    (println (part2 input-file))))