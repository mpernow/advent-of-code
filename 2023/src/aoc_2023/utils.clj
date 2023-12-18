(ns aoc-2023.utils
  (:require [clojure.string :as str]))

(defn parse-grid-chars-to-coords-char-tuple
  "Parses an input string of a multi-line grid of characters to a lazy sequence of [[x y] c] tuples.
  Optionally takes a function f, which is then applied to each value c."
  ([input] (parse-grid-chars-to-coords-char-tuple identity input))
  ([f input] (->> (str/split-lines input)
                  (map-indexed (fn [y line]
                                 (map-indexed (fn [x c] [[x y] (f c)]) line)))
                  (apply concat))))

(defn parse-grid-chars-to-coords-map
  "Parses an input string of a multi-line grid of characters to a map of {[x y] c}.
  Optionally takes a function f, which is then applied to each value c."
  ([input] (parse-grid-chars-to-coords-map identity input))
  ([f input] (into {} (parse-grid-chars-to-coords-char-tuple f input))))

(defn digit?
  [^Character c]
  (Character/isDigit c))

(defn space? [c] (= c \.))