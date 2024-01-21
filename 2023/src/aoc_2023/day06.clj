(ns aoc-2023.day06)

(defn distance-moved [total-time hold-time]
  (* hold-time (- total-time hold-time)))

(defn num-winners [total-time previous-best]
  (reduce (fn [[num-winners last-dist count-at-top] hold-time]
            (let [dist' (distance-moved total-time hold-time)
                  num-winners' (if (> dist' previous-best) (inc num-winners) num-winners)]
              (cond
                (< last-dist dist') [num-winners' dist' 1]
                (= last-dist dist') [num-winners' dist' (inc count-at-top)]
                :else (reduced (+ num-winners num-winners (- count-at-top))))))
          [0 0 1]
          (range 1 total-time)))

(defn solve [races]
  (transduce (map (fn [[time best]] (num-winners time best))) * races))

(defn -main []
  ;; Beacuse the input was so short, I didn't bother with parsing
  (let [input1 [[48 261] [93 1192] [84 1019] [66 1063]]]
    (println (solve input1)))
  (let [input2 [[48938466 261119210191063]]]
    (println (solve input2))))