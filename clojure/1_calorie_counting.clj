(ns advent-of-code-2022.1-calorie-counting
	(:require [clojure.java.io :as io]
						[clojure.string :as str]))

	
(defn str-to-ints
  [arr]
  (map #(Integer/parseInt %) arr))

(defn sum-calories[]
	(let [input (-> (io/as-relative-path "../inputs/day1.txt")
									slurp
									(str/split #"\n\n"))]
		(->> input
			(map #(str/split % #"\n"))
			(map str-to-ints)
			(map #(reduce + %))
			sort
			reverse
			(take 3))))

(defn solution[]
	(println (first (sum-calories)))
	(println (reduce + (sum-calories))))

(solution)
