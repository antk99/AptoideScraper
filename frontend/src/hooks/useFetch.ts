import { useState } from "react";

const DEFAULT_REQUEST_INIT: RequestInit = {
    method: "GET",
    headers: {
        "Content-Type": "application/json",
    },
};

function useFetch<T>(): {
    data: T | null;
    error: string | null;
    isLoading: boolean;
    fetchData: (url: string) => Promise<void>;
} {
    const [data, setData] = useState<T | null>(null);
    const [error, setError] = useState<string | null>(null);
    const [isLoading, setIsLoading] = useState<boolean>(false);

    const fetchData = async (url: string, requestInit: RequestInit = DEFAULT_REQUEST_INIT) => {
        setError(null);
        setData(null);
        setIsLoading(true);

        try {
            const response = await fetch(`${process.env.REACT_APP_API_HOSTNAME}/api/${url}`, requestInit);
            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || "Something went wrong."); // API error message
            }

            setData(data);
        } catch (error) {
            // JSON parsing error --> Response is not in JSON
            if (error instanceof SyntaxError) {
                setError("Something went wrong. Please try again later.");
            } else {
                setError(error instanceof Error ? error.message : "Failed to fetch data");
            }
        } finally {
            setIsLoading(false);
        }
    };

    return { data, error, isLoading, fetchData };
}

export default useFetch;
