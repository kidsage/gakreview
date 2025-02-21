'use client';

import { useState } from 'react';
import Header from '../components/Header';
import Search from '../components/Search';
import Map from '../components/Map';
import RestaurantList from '../components/RestaurantList';
import { restaurants } from '../data/restaurants'; // 임시 데이터 임포트
import styles from '../styles/Home.module.css';

export default function Home() {
    const [lat, setLat] = useState(37.5665); // 초기 위치: 서울
    const [lng, setLng] = useState(126.9780); // 초기 위치: 서울
    const [mapInstance, setMapInstance] = useState<any>(null); // 지도 객체 상태
    const [filteredRestaurants, setFilteredRestaurants] = useState<any[]>([]); // 검색된 식당 목록

    // 검색 처리 함수
    const handleSearch = async (query: string) => {
        try {
            const response = await fetch(
                `https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query=${encodeURIComponent(query)}`,
                {
                    headers: {
                        'X-NCP-APIGW-API-KEY-ID': process.env.NEXT_PUBLIC_NAVER_MAP_CLIENT_ID || '',
                        'X-NCP-APIGW-API-KEY': process.env.NEXT_PUBLIC_NAVER_MAP_CLIENT_SECRET || '',
                    },
                }
            );

            if (!response.ok) {
                throw new Error('네이버 지도 API 호출 실패');
            }

            const data = await response.json();
            console.log(data); // API 응답 확인

            if (data.addresses && data.addresses.length > 0) {
                const { x, y } = data.addresses[0]; // 경도(x), 위도(y)
                setLat(parseFloat(y)); // 위도 업데이트
                setLng(parseFloat(x)); // 경도 업데이트

                // 지도 이동
                if (mapInstance) {
                    const newCenter = new naver.maps.LatLng(parseFloat(y), parseFloat(x));
                    mapInstance.setCenter(newCenter);
                }

                // 임시 데이터에서 검색 결과 필터링
                const filtered = restaurants.filter((restaurant) =>
                    restaurant.name.toLowerCase().includes(query.toLowerCase())
                );
                setFilteredRestaurants(filtered);
            } else {
                alert('검색 결과가 없습니다.');
            }
        } catch (error) {
            console.error('검색 중 오류 발생:', error);
            alert('검색 중 오류가 발생했습니다.');
        }
    };

    // 지도 객체를 저장하는 콜백 함수
    const handleMapLoad = (map: any) => {
        setMapInstance(map);
    };

    return (
        <div className={styles.container}>
            <Header />
            <Search onSearch={handleSearch} />
            <Map lat={lat} lng={lng} onMapLoad={handleMapLoad} />
            <RestaurantList restaurants={filteredRestaurants} />
        </div>
    );
}