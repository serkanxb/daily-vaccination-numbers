-- First, fill countries with no valid records with 0
UPDATE vaccinations
SET daily_vaccinations = 0
WHERE daily_vaccinations IS NULL;

-- Next, fill in missing daily vaccination numbers with the median for each country
UPDATE vaccinations
SET daily_vaccinations = (
    SELECT MEDIAN(daily_vaccinations) OVER (PARTITION BY country)
    FROM vaccinations
    WHERE country = v.country
)
WHERE daily_vaccinations IS NULL;
