import React, { useEffect, useState } from 'react';

const useFetch = (url) => {
    const [data, setData] = useState(null);

    useEffect(() => {
        if (!url) return; // prevent fetch if url is empty or undefined

        fetch(url)
            .then((res) => res.json())
            .then((data) => setData(data))
            .catch((error) => {
                console.error('Fetch error:', error);
                setData(null);
            });
    }, [url]); // add url as dependency

    return [data];
};

export default useFetch;