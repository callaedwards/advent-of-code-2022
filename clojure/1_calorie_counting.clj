(ns advent-of-code-2022.1-calorie-counting)
	;(:require [advent-of-code-2022.common :as common]))

(defn Solution[]
	; (->
	; 	(slurp "inputs/day1.txt")
	; 	(clojure.string/split #"\n\n")

	; )
	(def input (clojure.string/split (slurp "inputs/day1.txt") #"\n\n"))
	(doseq [elf input]
		(let [i 0])
		(doseq [cal elf]
			(+ i (read-string cal))
		)
		(println(i))
	)

;			(println (reduce + )))
)

(Solution)